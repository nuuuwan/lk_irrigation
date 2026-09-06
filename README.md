# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_06:31:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 06:31:52 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:13:41 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-06 06:13:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:11:30 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:09:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:08:13 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:06:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:06:12 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-06 06:06:03 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.109 |  |
| 2026-09-06 06:05:57 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-06 06:05:36 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-09-06 06:05:12 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:05:10 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-09-06 06:04:46 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 06:04:34 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-09-06 06:04:16 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:04:07 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-09-06 06:04:03 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:03:51 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-06 06:03:25 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-06 06:03:00 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:51 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-06 06:02:48 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-09-06 06:02:40 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:23 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-09-06 06:02:21 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 06:02:21 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-06 06:02:19 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:16 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.052 |  |
| 2026-09-06 06:02:13 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:10 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:07 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:42 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:41 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.013 |  |
| 2026-09-06 06:01:31 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:15 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 05:55:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.171 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 06:04:34 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-09-06 06:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-09-06 06:04:07 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-09-06 06:13:41 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-06 06:06:12 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-06 06:05:57 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-06 06:02:21 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-06 06:03:51 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-06 06:02:21 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 06:04:46 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 06:04:16 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:15 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:19 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:05:12 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:31:52 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:31 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:13:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:03:00 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:11:30 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:09:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:01:42 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:06:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:07 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:04:03 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:48 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:08:13 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:13 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:02:10 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 06:03:25 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-06 06:01:41 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.013 |  |
| 2026-09-06 06:05:10 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-09-06 06:05:36 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-09-06 06:02:51 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-06 06:02:23 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-09-06 06:02:16 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.052 |  |
| 2026-09-06 06:06:03 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)