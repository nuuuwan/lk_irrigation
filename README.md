# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_10:38:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 10:38:57 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:22:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:22:25 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:17:24 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.026 |  |
| 2026-05-31 10:13:39 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.026 |  |
| 2026-05-31 10:11:04 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.029 |  |
| 2026-05-31 10:09:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:08:31 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.098 |  |
| 2026-05-31 10:07:58 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2026-05-31 10:07:36 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:06:36 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-05-31 10:06:21 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:05:51 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-31 10:05:39 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-05-31 10:04:49 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:04:42 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-31 10:04:07 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:04:00 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-31 10:03:39 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 10:03:33 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.207 |  |
| 2026-05-31 10:03:18 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:03:11 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-05-31 10:03:11 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | -0.089 |  |
| 2026-05-31 10:03:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-31 10:02:47 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:39 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:27 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:23 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:08 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:00 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.050 |  |
| 2026-05-31 10:01:47 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-31 10:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 10:01:17 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:00:53 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:00:44 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.051 |  |
| 2026-05-31 10:00:40 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:00:33 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 10:00:26 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:00:23 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-05-31 10:00:18 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 10:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.098 |  |
| 2026-05-31 10:04:00 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-31 10:03:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-31 10:03:39 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 10:04:42 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-31 10:00:33 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 10:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 10:00:53 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:39 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:08:31 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:00:18 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:08 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:38:57 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:23 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:22:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:04:07 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:09:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:47 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:02:27 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:06:21 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:00:40 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:22:25 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:01:17 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:04:49 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 10:06:36 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-05-31 10:05:51 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-31 10:07:58 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2026-05-31 10:00:23 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-05-31 10:03:11 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-05-31 10:01:47 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-31 10:13:39 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.026 |  |
| 2026-05-31 10:17:24 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.026 |  |
| 2026-05-31 10:11:04 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.029 |  |
| 2026-05-31 10:05:39 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-05-31 10:02:00 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.050 |  |
| 2026-05-31 10:00:44 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.051 |  |
| 2026-05-31 10:03:11 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | -0.089 |  |
| 2026-05-31 10:03:33 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)