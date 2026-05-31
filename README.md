# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_09:09:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 09:09:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:09:46 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.026 |  |
| 2026-05-31 09:09:18 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:08:39 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-05-31 09:07:53 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.022 |  |
| 2026-05-31 09:07:36 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-05-31 09:07:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-31 09:07:09 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.029 |  |
| 2026-05-31 09:06:54 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:05:41 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:05:27 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-05-31 09:05:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:04:30 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-05-31 09:04:22 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:04:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:03:45 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:03:40 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:03:12 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-05-31 09:02:47 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:46 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:44 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-05-31 09:02:38 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:02:26 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:25 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2026-05-31 09:02:21 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.151 |  |
| 2026-05-31 09:02:15 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.059 |  |
| 2026-05-31 09:02:13 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.121 |  |
| 2026-05-31 09:02:13 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 09:02:11 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-31 09:02:08 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-31 09:01:58 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:41 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:30 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.022 |  |
| 2026-05-31 09:01:11 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.115 |  |
| 2026-05-31 09:00:15 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-05-31 08:34:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 09:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.115 |  |
| 2026-05-31 09:02:08 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-31 09:02:11 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-31 09:02:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 09:07:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-31 09:02:13 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:04:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:58 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:47 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:46 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:09:18 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:30 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:09:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:05:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:41 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:03:40 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:11 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:02:26 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:01:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:06:54 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 09:07:36 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-05-31 09:08:39 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-05-31 09:04:22 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:03:45 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:05:41 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:02:38 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-05-31 09:05:27 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-05-31 09:03:12 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-05-31 09:00:15 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-05-31 09:02:44 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-05-31 09:07:53 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.022 |  |
| 2026-05-31 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.022 |  |
| 2026-05-31 09:02:25 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2026-05-31 09:09:46 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.026 |  |
| 2026-05-31 09:07:09 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.029 |  |
| 2026-05-31 09:04:30 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-05-31 09:02:15 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.059 |  |
| 2026-05-31 09:02:13 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.121 |  |
| 2026-05-31 09:02:21 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)