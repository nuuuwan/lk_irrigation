# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_22:10:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,933 measurements** from **39** stations.
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
| 2026-10-05 22:10:43 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-05 22:10:01 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.047 |  |
| 2026-10-05 22:07:41 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-05 22:07:35 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 22:07:13 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.028 |  |
| 2026-10-05 22:06:51 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | -0.330 |  |
| 2026-10-05 22:06:34 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 22:06:18 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.029 |  |
| 2026-10-05 22:06:13 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-05 22:06:00 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-05 22:05:48 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:05:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:05:22 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-05 22:04:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-05 22:04:03 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.393 |  |
| 2026-10-05 22:03:54 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 22:03:42 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 22:03:23 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.069 |  |
| 2026-10-05 22:03:11 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-10-05 22:03:00 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-10-05 22:02:47 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:02:46 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:02:31 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-10-05 22:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:02:11 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-10-05 22:02:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.052 |  |
| 2026-10-05 22:01:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:01:01 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:00:54 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:00:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-05 22:00:23 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 22:03:00 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-10-05 22:03:11 | Glencourse (Kelani Ganga) | 12.91 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-10-05 22:02:11 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-10-05 22:10:43 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-05 22:05:22 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-05 21:01:34 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-05 22:00:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-05 21:07:37 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 22:07:35 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 22:07:41 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-05 22:04:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 22:06:34 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 22:03:42 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 22:03:54 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 21:16:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:01:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:00:54 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:05:48 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:01:01 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:02:47 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:00:23 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:05:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:02:46 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-05 22:06:13 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-05 22:06:00 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-05 22:02:31 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-10-05 22:07:13 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.028 |  |
| 2026-10-05 22:06:18 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.029 |  |
| 2026-10-05 22:10:01 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.047 |  |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-05 22:02:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.052 |  |
| 2026-10-05 21:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2026-10-05 22:03:23 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.069 |  |
| 2026-10-05 22:06:51 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | -0.330 |  |
| 2026-10-05 22:04:03 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.393 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)