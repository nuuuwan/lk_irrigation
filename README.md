# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_21:07:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 21:07:59 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:07:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 21:07:41 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:07:31 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:07:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-09-30 21:06:58 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-09-30 21:06:38 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-09-30 21:06:26 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-09-30 21:06:26 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.094 |  |
| 2026-09-30 21:06:13 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:05:15 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:05:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:04:33 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-09-30 21:04:00 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-09-30 21:03:49 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.011 |  |
| 2026-09-30 21:03:25 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-30 21:03:19 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:53 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:53 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:02:36 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-30 21:02:31 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:22 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:19 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2026-09-30 21:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-09-30 21:02:10 | Hanwella (Kelani Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-09-30 21:02:03 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:01:58 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:01:27 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.145 |  |
| 2026-09-30 21:01:22 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:00:53 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:00:30 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 21:06:26 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 21:02:36 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-30 20:02:50 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-30 21:07:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 21:00:53 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:00:30 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:07:59 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:07:31 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:03:19 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:05:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:03 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:22 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:07:41 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:31 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:05:15 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:02:53 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 21:06:13 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:01:58 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:01:22 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:02:53 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-09-30 21:03:49 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.011 |  |
| 2026-09-30 21:04:00 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-09-30 21:07:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-09-30 20:08:32 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-09-30 21:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-09-30 21:03:25 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-30 21:06:58 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-09-30 21:04:33 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-09-30 21:06:38 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-09-30 21:02:10 | Hanwella (Kelani Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-09-30 21:02:19 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2026-09-30 21:06:26 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.094 |  |
| 2026-09-30 21:01:27 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)