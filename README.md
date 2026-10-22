# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_08:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,702 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 08:13:08 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:09:56 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:09:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:08:16 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:08:07 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-10-22 08:07:26 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:06:57 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.100 |  |
| 2026-10-22 08:06:26 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-22 08:05:58 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-22 08:05:45 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.067 |  |
| 2026-10-22 08:05:44 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.087 |  |
| 2026-10-22 08:04:25 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.114 |  |
| 2026-10-22 08:04:20 | Horowpothana (Yan Oya) | 3.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 08:04:19 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:04:18 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.129 |  |
| 2026-10-22 08:04:08 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-22 08:04:04 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.073 |  |
| 2026-10-22 08:03:33 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-22 08:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-10-22 08:03:25 | Giriulla (Maha Oya) | 2.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 08:03:25 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -72.000 |  |
| 2026-10-22 08:03:23 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -72.000 |  |
| 2026-10-22 08:03:21 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-10-22 08:03:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:03:14 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:03:13 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-22 08:03:12 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 08:03:04 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 08:03:00 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.254 |  |
| 2026-10-22 08:02:56 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-10-22 08:02:53 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-22 08:02:49 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:02:48 | Moragaswewa (Deduru Oya) | 4.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 08:02:40 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-10-22 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 08:02:25 | Ellagawa (Kalu Ganga) | 7.22 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-10-22 08:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:01:10 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.031 |  |
| 2026-10-22 08:00:39 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.169 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 08:06:26 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-22 08:02:25 | Ellagawa (Kalu Ganga) | 7.22 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-10-22 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 08:03:13 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-22 08:04:08 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-22 08:05:58 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-22 08:03:25 | Giriulla (Maha Oya) | 2.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 07:03:01 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 08:03:12 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 08:04:20 | Horowpothana (Yan Oya) | 3.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 08:03:04 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 08:02:48 | Moragaswewa (Deduru Oya) | 4.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 08:09:56 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:13:08 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:03:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:11:41 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:14:24 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-10-22 08:07:26 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:04:19 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:02:49 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:03:14 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-22 08:03:33 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-22 08:02:40 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-10-22 08:02:53 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-22 08:03:21 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-10-22 08:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-10-22 08:01:10 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.031 |  |
| 2026-10-22 08:02:56 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-10-22 08:05:45 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.067 |  |
| 2026-10-22 08:08:07 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-10-22 08:04:04 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.073 |  |
| 2026-10-22 08:05:44 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.087 |  |
| 2026-10-22 08:06:57 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.100 |  |
| 2026-10-22 08:04:25 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.114 |  |
| 2026-10-22 08:04:18 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.129 |  |
| 2026-10-22 08:00:39 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.169 |  |
| 2026-10-22 08:03:00 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | -0.254 |  |
| 2026-10-22 08:03:25 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)