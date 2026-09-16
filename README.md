# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_09:09:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,313 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 09:09:57 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:09:14 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:08:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:08:32 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.057 |  |
| 2026-09-16 09:08:26 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | -0.043 |  |
| 2026-09-16 09:07:22 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.050 |  |
| 2026-09-16 09:07:18 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:06:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.112 |  |
| 2026-09-16 09:06:07 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 09:04:56 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 09:04:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-09-16 09:04:33 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.061 |  |
| 2026-09-16 09:04:11 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:04:03 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:03:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:03:42 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:03:22 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.078 |  |
| 2026-09-16 09:03:02 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 09:02:54 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-09-16 09:02:48 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-16 09:02:31 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | -0.022 |  |
| 2026-09-16 09:02:25 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:14 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-16 09:02:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:03 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:00 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-09-16 09:02:00 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-16 09:01:47 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:01:41 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:01:26 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:00:53 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:00:44 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:00:23 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-16 09:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 09:02:00 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-09-16 09:02:48 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-16 09:00:23 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-16 09:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 09:03:02 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 09:01:26 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 09:06:07 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 09:04:56 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 09:00:53 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:01:41 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:03 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:01:47 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:25 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:07:18 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-16 08:03:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:00:44 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:03:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:09:57 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:08:26 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 09:02:14 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-16 09:02:00 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-16 09:02:54 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-09-16 09:04:11 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:09:14 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:03:42 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:08:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:04:03 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-09-16 09:02:31 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | -0.022 |  |
| 2026-09-16 09:04:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-09-16 08:05:53 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.031 |  |
| 2026-09-16 09:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | -0.043 |  |
| 2026-09-16 09:07:22 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.050 |  |
| 2026-09-16 09:08:32 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.057 |  |
| 2026-09-16 09:04:33 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.061 |  |
| 2026-09-16 09:03:22 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.078 |  |
| 2026-09-16 08:05:42 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.103 |  |
| 2026-09-16 09:06:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)