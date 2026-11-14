# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_11:13:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,538 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 11:13:50 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.017 |  |
| 2026-11-14 11:13:21 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:10:13 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-14 11:08:49 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:08:09 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.095 |  |
| 2026-11-14 11:08:08 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.062 |  |
| 2026-11-14 11:07:58 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.014 | 🔺 Rising |
| 2026-11-14 11:07:58 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:07:48 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.012 |  |
| 2026-11-14 11:06:01 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | -0.052 |  |
| 2026-11-14 11:05:54 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:05:45 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.036 |  |
| 2026-11-14 11:05:34 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:04:38 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-14 11:04:29 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -1.021 |  |
| 2026-11-14 11:04:28 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.029 |  |
| 2026-11-14 11:04:22 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:04:21 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 11:07:58 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.014 | 🔺 Rising |
| 2026-11-14 11:05:45 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.036 |  |
| 2026-11-14 11:06:01 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | -0.052 |  |
| 2026-11-14 11:04:38 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-14 11:01:22 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:04:22 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:03:04 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:01:59 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:02:33 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-14 10:03:12 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:02:49 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:01:34 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:02:06 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:08:49 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 11:07:58 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:13:21 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:05:34 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:03:26 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:05:54 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-14 10:01:42 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:00:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:01:11 | Kuda Oya (Kirindi Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-14 11:07:48 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.012 |  |
| 2026-11-14 11:13:50 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.017 |  |
| 2026-11-14 11:10:13 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-14 11:03:23 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-11-14 11:02:51 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-11-14 11:00:46 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.022 |  |
| 2026-11-14 11:04:21 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-11-14 11:04:28 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.029 |  |
| 2026-11-14 11:02:31 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.033 |  |
| 2026-11-14 11:01:30 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.041 |  |
| 2026-11-14 11:08:08 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.062 |  |
| 2026-11-14 11:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.080 |  |
| 2026-11-14 11:03:21 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.092 |  |
| 2026-11-14 11:08:09 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.095 |  |
| 2026-11-14 11:02:54 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.143 |  |
| 2026-11-14 11:04:29 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -1.021 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)