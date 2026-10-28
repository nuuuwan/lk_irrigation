# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_11:15:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,221 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 11:15:03 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-28 11:10:27 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 11:07:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-10-28 11:07:36 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:34 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:29 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 11:07:11 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:06:53 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.048 |  |
| 2026-10-28 11:06:09 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.065 |  |
| 2026-10-28 11:06:05 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.058 |  |
| 2026-10-28 11:05:27 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:04:54 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-28 11:04:47 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.028 |  |
| 2026-10-28 11:04:42 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | -0.069 |  |
| 2026-10-28 11:04:35 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:04:15 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.041 |  |
| 2026-10-28 11:04:10 | Ellagawa (Kalu Ganga) | 10.43 | 🟡 Alert | -0.010 |  |
| 2026-10-28 11:04:02 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.099 |  |
| 2026-10-28 11:03:53 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-10-28 11:03:21 | Rathnapura (Kalu Ganga) | 6.34 | 🟡 Alert | -0.071 |  |
| 2026-10-28 11:03:10 | Putupaula (Kalu Ganga) | 3.63 | 🟡 Alert | 0.000 |  |
| 2026-10-28 11:02:58 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 11:02:53 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-28 11:02:39 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.129 |  |
| 2026-10-28 11:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 11:02:24 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.030 |  |
| 2026-10-28 11:02:21 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:02:19 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:01:54 | Thanthirimale (Malwathu Oya) | 2.24 | 🟢 Normal | -0.059 |  |
| 2026-10-28 11:01:47 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.105 |  |
| 2026-10-28 11:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:01:30 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:01:22 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-28 11:01:15 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:01:14 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:01:08 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-28 11:00:22 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-10-28 11:00:04 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 11:04:54 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-10-28 11:07:29 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 11:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.77 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 11:03:10 | Putupaula (Kalu Ganga) | 3.63 | 🟡 Alert | 0.000 |  |
| 2026-10-28 11:04:10 | Ellagawa (Kalu Ganga) | 10.43 | 🟡 Alert | -0.010 |  |
| 2026-10-28 11:02:24 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.030 |  |
| 2026-10-28 11:06:09 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.065 |  |
| 2026-10-28 11:03:21 | Rathnapura (Kalu Ganga) | 6.34 | 🟡 Alert | -0.071 |  |
| 2026-10-28 11:01:47 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.105 |  |
| 2026-10-28 11:00:22 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-10-28 11:15:03 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-28 11:02:58 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 11:02:53 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-28 11:10:27 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 11:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:11 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:02:19 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:04:35 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:36 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:01:30 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:01:14 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:34 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-28 11:07:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-10-28 11:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:01:15 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:02:21 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:05:27 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 11:00:04 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-10-28 11:01:22 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-28 11:01:08 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-28 11:04:47 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.028 |  |
| 2026-10-28 11:03:53 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-10-28 11:04:15 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.041 |  |
| 2026-10-28 11:06:53 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.048 |  |
| 2026-10-28 11:06:05 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.058 |  |
| 2026-10-28 11:01:54 | Thanthirimale (Malwathu Oya) | 2.24 | 🟢 Normal | -0.059 |  |
| 2026-10-28 11:04:42 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | -0.069 |  |
| 2026-10-28 11:04:02 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.099 |  |
| 2026-10-28 11:02:39 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)