# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_05:38:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 05:38:07 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2026-10-10 05:24:48 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.104 |  |
| 2026-10-10 05:24:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-10-10 05:22:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-10-10 05:17:29 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.077 |  |
| 2026-10-10 05:16:31 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.023 |  |
| 2026-10-10 05:14:17 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.052 |  |
| 2026-10-10 05:12:20 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-10 05:11:47 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-10 05:11:21 | Pitabeddara (Nilwala Ganga) | 2.01 | 🟢 Normal | -3.349 |  |
| 2026-10-10 05:10:38 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -3.349 |  |
| 2026-10-10 05:07:40 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.060 |  |
| 2026-10-10 05:07:06 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-10 05:06:22 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.022 |  |
| 2026-10-10 05:05:51 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.019 |  |
| 2026-10-10 05:05:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:12 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:02 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.049 |  |
| 2026-10-10 05:05:00 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-10 05:04:48 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.092 |  |
| 2026-10-10 05:04:40 | Giriulla (Maha Oya) | 4.34 | 🟢 Normal | -0.109 |  |
| 2026-10-10 05:03:54 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -36.000 |  |
| 2026-10-10 05:03:52 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | -36.000 |  |
| 2026-10-10 05:03:25 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-10 05:03:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.175 |  |
| 2026-10-10 05:02:48 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:02:37 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-10 05:02:26 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-10-10 05:02:23 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | -0.021 |  |
| 2026-10-10 05:01:56 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-10 05:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | -0.246 |  |
| 2026-10-10 05:01:49 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.104 |  |
| 2026-10-10 05:01:21 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-10 05:01:16 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-10-10 05:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 05:01:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:00:40 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:00:10 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 05:03:25 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-10 05:02:26 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-10-10 05:05:00 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-10 05:02:37 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-10 05:07:06 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-10 05:01:21 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-10 05:00:10 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-10 04:31:56 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-10 05:01:56 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 05:12:20 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 05:01:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:12 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:02:48 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:03:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:00:40 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 05:38:07 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2026-10-10 05:05:51 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.019 |  |
| 2026-10-10 05:11:47 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-10 05:02:23 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | -0.021 |  |
| 2026-10-10 05:06:22 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.022 |  |
| 2026-10-10 05:22:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-10-10 05:16:31 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.023 |  |
| 2026-10-10 05:24:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-10-10 05:05:02 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.049 |  |
| 2026-10-10 05:14:17 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.052 |  |
| 2026-10-10 05:07:40 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.060 |  |
| 2026-10-10 05:17:29 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.077 |  |
| 2026-10-10 05:04:48 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.092 |  |
| 2026-10-10 05:24:48 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.104 |  |
| 2026-10-10 05:04:40 | Giriulla (Maha Oya) | 4.34 | 🟢 Normal | -0.109 |  |
| 2026-10-10 05:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.175 |  |
| 2026-10-10 05:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | -0.246 |  |
| 2026-10-10 05:11:21 | Pitabeddara (Nilwala Ganga) | 2.01 | 🟢 Normal | -3.349 |  |
| 2026-10-10 05:03:54 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)