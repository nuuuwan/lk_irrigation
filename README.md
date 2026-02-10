# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_09:31:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 09:31:35 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:18:49 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:12:38 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-02-10 09:10:52 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:09:44 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:07:44 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:06:57 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:06:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:05:39 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:05:31 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-10 09:05:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-02-10 09:04:57 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:55 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:19 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:17 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-10 09:04:15 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:03:55 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.069 |  |
| 2026-02-10 09:03:50 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-02-10 09:03:48 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.247 |  |
| 2026-02-10 09:03:33 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-02-10 09:03:12 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.049 |  |
| 2026-02-10 09:03:08 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-10 09:02:49 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:49 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:41 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:36 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:19 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:05 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:01:37 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:01:31 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-02-10 09:01:17 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:00:53 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.051 |  |
| 2026-02-10 09:00:43 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:00:31 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:00:17 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.049 |  |
| 2026-02-10 08:39:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 09:04:17 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-10 09:05:31 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-10 09:03:08 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-10 09:02:19 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:15 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:31:35 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:05:39 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:19 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:49 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:36 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:05 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:55 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:05:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:01:17 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:41 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:49 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:02:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:04:57 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:00:31 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:18:49 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:01:37 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:07:44 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 09:12:38 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-02-10 09:06:57 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:10:52 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:09:44 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:06:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-10 09:03:33 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-02-10 09:01:31 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-02-10 09:03:50 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-02-10 09:00:17 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.049 |  |
| 2026-02-10 09:03:12 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.049 |  |
| 2026-02-10 09:00:53 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.051 |  |
| 2026-02-10 09:03:55 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.069 |  |
| 2026-02-10 09:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-02-10 09:03:48 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)