# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_22:03:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 22:03:37 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:03:31 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-28 22:03:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:03:11 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:02:54 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:02:44 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:02:43 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-28 22:02:39 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 22:02:39 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 22:02:39 | Ellagawa (Kalu Ganga) | 10.31 | 🟡 Alert | -0.035 |  |
| 2026-10-28 22:02:35 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:02:16 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:02:11 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | -0.039 |  |
| 2026-10-28 22:01:54 | Moragaswewa (Deduru Oya) | 2.57 | 🟢 Normal | -0.090 |  |
| 2026-10-28 22:01:44 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.053 |  |
| 2026-10-28 22:01:30 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:01:11 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 22:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 21:03:35 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-28 22:01:11 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 21:03:35 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 21:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 21:01:57 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 22:02:39 | Ellagawa (Kalu Ganga) | 10.31 | 🟡 Alert | -0.035 |  |
| 2026-10-28 21:05:01 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | -0.055 |  |
| 2026-10-28 21:01:08 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.069 |  |
| 2026-10-28 21:06:17 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-28 21:04:16 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 21:00:19 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-28 21:06:22 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 22:02:39 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 22:02:39 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 22:01:30 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:12:01 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:05:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:03:11 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:02:44 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:03:37 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:03:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:04:57 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 22:02:16 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:02:35 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:02:54 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-28 22:02:43 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-28 22:03:31 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-28 21:02:41 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | -0.020 |  |
| 2026-10-28 21:03:01 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-10-28 21:07:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-28 22:02:11 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | -0.039 |  |
| 2026-10-28 21:02:07 | Pitabeddara (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.049 |  |
| 2026-10-28 22:01:44 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.053 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 22:01:54 | Moragaswewa (Deduru Oya) | 2.57 | 🟢 Normal | -0.090 |  |
| 2026-10-28 21:10:54 | Urawa (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)