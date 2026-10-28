# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_07:04:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Ellagawa — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 07:04:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.074 |  |
| 2026-10-28 07:03:57 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:03:56 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-10-28 07:03:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:03:05 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:02:47 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.029 |  |
| 2026-10-28 07:02:46 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.030 |  |
| 2026-10-28 07:02:41 | Thanthirimale (Malwathu Oya) | 2.43 | 🟢 Normal | -0.022 |  |
| 2026-10-28 07:02:41 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.061 |  |
| 2026-10-28 07:02:35 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:02:14 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:02:11 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-10-28 07:01:53 | Moragaswewa (Deduru Oya) | 3.17 | 🟢 Normal | -0.121 |  |
| 2026-10-28 07:01:48 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.071 |  |
| 2026-10-28 07:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:01:43 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 07:01:34 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.130 |  |
| 2026-10-28 07:01:25 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:01:08 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:00:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.186 |  |
| 2026-10-28 07:00:35 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:00:24 | Horowpothana (Yan Oya) | 3.34 | 🟢 Normal | -0.035 |  |
| 2026-10-28 06:37:32 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:25:56 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 06:02:34 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-28 07:01:43 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 06:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.82 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-28 06:10:46 | Ellagawa (Kalu Ganga) | 10.46 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 06:01:57 | Putupaula (Kalu Ganga) | 3.58 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 07:02:47 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.029 |  |
| 2026-10-28 07:02:46 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.030 |  |
| 2026-10-28 07:01:48 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.071 |  |
| 2026-10-28 06:01:38 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.073 |  |
| 2026-10-28 06:04:36 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-28 06:01:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-28 06:05:49 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 07:02:14 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:01:08 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:03:57 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:04:22 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:01:25 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:04:13 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:03:05 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 07:03:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:00:30 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:00:35 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:02:35 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-28 07:02:11 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-10-28 06:00:37 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-10-28 07:02:41 | Thanthirimale (Malwathu Oya) | 2.43 | 🟢 Normal | -0.022 |  |
| 2026-10-28 07:03:56 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-10-28 07:00:24 | Horowpothana (Yan Oya) | 3.34 | 🟢 Normal | -0.035 |  |
| 2026-10-28 07:02:41 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.061 |  |
| 2026-10-28 06:01:43 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | -0.063 |  |
| 2026-10-28 07:04:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.074 |  |
| 2026-10-28 06:02:32 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.079 |  |
| 2026-10-28 06:03:59 | Glencourse (Kelani Ganga) | 11.85 | 🟢 Normal | -0.088 |  |
| 2026-10-28 06:01:13 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.096 |  |
| 2026-10-28 07:01:53 | Moragaswewa (Deduru Oya) | 3.17 | 🟢 Normal | -0.121 |  |
| 2026-10-28 07:01:34 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.130 |  |
| 2026-10-28 06:13:46 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.166 |  |
| 2026-10-28 07:00:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)