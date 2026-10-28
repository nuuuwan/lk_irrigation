# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_09:04:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,125 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:04:12 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 09:04:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:03:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.096 |  |
| 2026-10-28 09:03:24 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:23 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-10-28 09:03:14 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:13 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:02:55 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-10-28 09:02:50 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 0.000 |  |
| 2026-10-28 09:02:29 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:24 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:14 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.073 |  |
| 2026-10-28 09:02:12 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:09 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:05 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:01 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:01:40 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-10-28 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:01:11 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 09:00:46 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 08:42:20 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 08:06:46 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 09:01:11 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 08:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-28 09:04:12 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 09:02:50 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | 0.000 |  |
| 2026-10-28 08:05:28 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.019 |  |
| 2026-10-28 08:11:35 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.028 |  |
| 2026-10-28 09:02:14 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.073 |  |
| 2026-10-28 08:07:18 | Rathnapura (Kalu Ganga) | 6.56 | 🟡 Alert | -0.076 |  |
| 2026-10-28 08:01:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:05 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:14 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:12 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:03:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:00:46 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:02:01 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 09:04:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:06:02 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:13 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-28 09:03:24 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:01:37 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 08:01:57 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-28 09:01:40 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-10-28 08:10:14 | Galgamuwa (Mee Oya) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-10-28 09:03:23 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-10-28 08:03:25 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-28 09:02:55 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-10-28 08:21:07 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-10-28 08:09:23 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.038 |  |
| 2026-10-28 08:04:25 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | -0.045 |  |
| 2026-10-28 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.047 |  |
| 2026-10-28 09:02:09 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:24 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-10-28 09:02:29 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-28 08:00:03 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.060 |  |
| 2026-10-28 08:02:56 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | -0.062 |  |
| 2026-10-28 09:03:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)