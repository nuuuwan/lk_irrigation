# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_04:14:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 04:14:54 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:07:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-31 04:06:58 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:06:12 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-10-31 04:06:08 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-10-31 04:05:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:05:27 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-31 04:05:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:05:03 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 04:04:45 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-31 04:04:36 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-10-31 04:04:33 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-31 04:04:16 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:04:07 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:03:58 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | -0.019 |  |
| 2026-10-31 04:03:49 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.042 |  |
| 2026-10-31 04:03:36 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.030 |  |
| 2026-10-31 04:02:58 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-31 04:02:57 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.121 |  |
| 2026-10-31 04:02:37 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:30 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.049 |  |
| 2026-10-31 04:02:27 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 04:02:15 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:11 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:00:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-10-31 04:00:56 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:00:49 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 03:56:39 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 04:00:49 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 03:06:07 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.016 |  |
| 2026-10-31 03:05:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -3.130 |  |
| 2026-10-31 04:04:45 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-31 04:07:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-31 04:02:58 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-31 04:02:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 04:02:27 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 04:05:03 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 04:00:56 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:06:58 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:05:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:04:07 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:15 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:04:16 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:10:35 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:11 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:14:54 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:05:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:02:26 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-31 04:04:33 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-31 04:06:12 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-10-31 04:03:58 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | -0.019 |  |
| 2026-10-31 04:04:36 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-10-31 04:05:27 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 04:00:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-10-31 04:03:36 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.030 |  |
| 2026-10-31 03:07:42 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | -0.032 |  |
| 2026-10-31 03:08:42 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.037 |  |
| 2026-10-31 04:06:08 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-10-31 04:03:49 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.042 |  |
| 2026-10-31 04:02:30 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.049 |  |
| 2026-10-31 04:02:57 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.121 |  |
| 2026-10-31 03:09:54 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)