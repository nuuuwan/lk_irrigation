# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_05:07:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-10-10 05:01:49 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.035 |  |
| 2026-10-10 05:01:21 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-10 05:01:16 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-10-10 05:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 05:01:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:00:40 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:00:10 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-10 04:31:56 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.047 | 🔺 Rising |

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
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 05:01:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:12 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:02:48 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:03:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 04:02:53 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:00:40 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-10 04:20:01 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-10-10 05:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 04:24:13 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.016 |  |
| 2026-10-10 05:05:51 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.019 |  |
| 2026-10-10 04:07:12 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-10-10 03:05:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-10-10 05:02:23 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | -0.021 |  |
| 2026-10-10 05:06:22 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.022 |  |
| 2026-10-10 04:03:55 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.031 |  |
| 2026-10-10 05:01:49 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.035 |  |
| 2026-10-10 05:05:02 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.049 |  |
| 2026-10-10 04:05:06 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-10-10 03:04:26 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.057 |  |
| 2026-10-10 05:07:40 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.060 |  |
| 2026-10-10 05:04:48 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.092 |  |
| 2026-10-10 05:04:40 | Giriulla (Maha Oya) | 4.34 | 🟢 Normal | -0.109 |  |
| 2026-10-10 04:02:51 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.119 |  |
| 2026-10-10 05:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.175 |  |
| 2026-10-10 05:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | -0.246 |  |
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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)