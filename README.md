# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_08:21:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Ellagawa — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 08:21:07 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-10-28 08:18:50 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.028 |  |
| 2026-10-28 08:11:49 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:11:35 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.028 |  |
| 2026-10-28 08:10:14 | Galgamuwa (Mee Oya) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-10-28 08:09:23 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.038 |  |
| 2026-10-28 08:08:27 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-10-28 08:07:38 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.019 |  |
| 2026-10-28 08:07:18 | Rathnapura (Kalu Ganga) | 6.56 | 🟡 Alert | -0.076 |  |
| 2026-10-28 08:06:46 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 08:06:02 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:06:01 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:05:55 | Putupaula (Kalu Ganga) | 3.61 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 08:05:28 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.019 |  |
| 2026-10-28 08:05:04 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | -0.076 |  |
| 2026-10-28 08:04:55 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.129 |  |
| 2026-10-28 08:04:31 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.013 |  |
| 2026-10-28 08:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-28 08:04:25 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | -0.045 |  |
| 2026-10-28 08:04:15 | Moragaswewa (Deduru Oya) | 3.09 | 🟢 Normal | -0.077 |  |
| 2026-10-28 08:04:02 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:03:44 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:03:25 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-28 08:02:56 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | -0.062 |  |
| 2026-10-28 08:02:44 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 3.931 | 🔺 Rising |
| 2026-10-28 08:02:34 | Giriulla (Maha Oya) | 2.32 | 🟢 Normal | -0.050 |  |
| 2026-10-28 08:02:20 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.043 |  |
| 2026-10-28 08:02:12 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.061 |  |
| 2026-10-28 08:02:12 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-28 08:02:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:02:06 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:01:57 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-28 08:01:45 | Thanthirimale (Malwathu Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-10-28 08:01:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:01:37 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:01:04 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:01:03 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.091 |  |
| 2026-10-28 08:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:00:03 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 08:06:46 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 07:16:33 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 08:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-28 08:02:44 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 3.931 | 🔺 Rising |
| 2026-10-28 08:05:55 | Putupaula (Kalu Ganga) | 3.61 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 08:05:28 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.019 |  |
| 2026-10-28 08:11:35 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.028 |  |
| 2026-10-28 08:05:04 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | -0.076 |  |
| 2026-10-28 08:07:18 | Rathnapura (Kalu Ganga) | 6.56 | 🟡 Alert | -0.076 |  |
| 2026-10-28 08:01:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:01:04 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:02:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:04:02 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:11:49 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:08:27 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-10-28 08:06:02 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:03:44 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:01:37 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:02:06 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:01:57 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-28 08:04:31 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.013 |  |
| 2026-10-28 08:10:14 | Galgamuwa (Mee Oya) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-10-28 08:07:38 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.019 |  |
| 2026-10-28 08:02:12 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-28 08:03:25 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-28 08:18:50 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.028 |  |
| 2026-10-28 08:01:45 | Thanthirimale (Malwathu Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-10-28 08:21:07 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-10-28 08:09:23 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.038 |  |
| 2026-10-28 08:02:20 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.043 |  |
| 2026-10-28 08:04:25 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | -0.045 |  |
| 2026-10-28 08:02:34 | Giriulla (Maha Oya) | 2.32 | 🟢 Normal | -0.050 |  |
| 2026-10-28 08:00:03 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.060 |  |
| 2026-10-28 08:02:12 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.061 |  |
| 2026-10-28 08:02:56 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | -0.062 |  |
| 2026-10-28 08:04:15 | Moragaswewa (Deduru Oya) | 3.09 | 🟢 Normal | -0.077 |  |
| 2026-10-28 08:01:03 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.091 |  |
| 2026-10-28 08:04:55 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)