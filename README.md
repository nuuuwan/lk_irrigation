# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_05:32:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,270 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 05:32:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | 2.000 | 🔺 Rising |
| 2026-10-15 05:31:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | 2.000 | 🔺 Rising |
| 2026-10-15 05:23:37 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.048 |  |
| 2026-10-15 05:22:15 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 05:18:50 | Rathnapura (Kalu Ganga) | 4.19 | 🟢 Normal | -0.118 |  |
| 2026-10-15 05:11:35 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.018 |  |
| 2026-10-15 05:11:35 | Magura (Kalu Ganga) | 3.99 | 🟢 Normal | -0.100 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 05:03:50 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 05:32:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | 2.000 | 🔺 Rising |
| 2026-10-15 05:02:29 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-10-15 05:23:37 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.048 |  |
| 2026-10-15 04:03:39 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-15 05:00:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 2.653 | 🔺 Rising |
| 2026-10-15 02:01:20 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-10-15 05:06:35 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-15 05:04:15 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-15 05:03:40 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-15 05:08:41 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 05:22:15 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 05:03:23 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 05:02:07 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 05:02:41 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 04:05:57 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-15 05:09:55 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 05:04:19 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 05:01:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 05:03:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 05:06:48 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 05:06:02 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.005 |  |
| 2026-10-15 04:12:46 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-15 05:01:12 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-15 05:07:37 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-15 05:03:48 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-10-15 05:04:21 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -0.012 |  |
| 2026-10-15 05:11:35 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.018 |  |
| 2026-10-15 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-10-15 05:03:54 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.039 |  |
| 2026-10-15 05:11:35 | Magura (Kalu Ganga) | 3.99 | 🟢 Normal | -0.100 |  |
| 2026-10-15 05:10:23 | Holombuwa (Kelani Ganga) | 1.96 | 🟢 Normal | -0.115 |  |
| 2026-10-15 05:03:12 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.116 |  |
| 2026-10-15 05:18:50 | Rathnapura (Kalu Ganga) | 4.19 | 🟢 Normal | -0.118 |  |
| 2026-10-15 05:06:10 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.150 |  |
| 2026-10-15 05:04:32 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)