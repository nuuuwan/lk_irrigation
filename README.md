# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_11:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 11:18:27 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.078 |  |
| 2026-10-10 11:15:35 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:14:02 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.008 |  |
| 2026-10-10 11:13:28 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.028 |  |
| 2026-10-10 11:11:23 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:10:50 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:09:24 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.066 |  |
| 2026-10-10 11:07:19 | Badalgama (Maha Oya) | 4.61 | 🟢 Normal | -0.107 |  |
| 2026-10-10 11:07:08 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.019 |  |
| 2026-10-10 11:06:25 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.226 |  |
| 2026-10-10 11:06:13 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 11:07:08 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.019 |  |
| 2026-10-10 11:02:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-10 11:01:45 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-10 11:00:56 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-10 11:01:41 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:15:35 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:03:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:00:50 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:05:46 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:03:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:03:25 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:11:23 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:01:44 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:03:21 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:01:35 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-10 11:14:02 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.008 |  |
| 2026-10-10 11:06:13 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-10 11:00:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-10 11:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-10 11:03:00 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-10-10 11:06:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-10 11:03:14 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-10 11:01:28 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-10-10 11:13:28 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.028 |  |
| 2026-10-10 11:03:08 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | -0.030 |  |
| 2026-10-10 11:04:38 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | -0.031 |  |
| 2026-10-10 11:03:52 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.031 |  |
| 2026-10-10 11:04:00 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-10-10 11:03:58 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-10-10 11:03:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.033 |  |
| 2026-10-10 11:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.039 |  |
| 2026-10-10 11:05:04 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | -0.050 |  |
| 2026-10-10 11:09:24 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.066 |  |
| 2026-10-10 11:03:27 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.072 |  |
| 2026-10-10 11:18:27 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.078 |  |
| 2026-10-10 11:01:44 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.091 |  |
| 2026-10-10 11:07:19 | Badalgama (Maha Oya) | 4.61 | 🟢 Normal | -0.107 |  |
| 2026-10-10 11:02:18 | Giriulla (Maha Oya) | 3.50 | 🟢 Normal | -0.110 |  |
| 2026-10-10 11:06:25 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.226 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)