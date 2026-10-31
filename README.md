# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_11:18:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 11:18:14 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | -0.025 |  |
| 2026-10-31 11:16:10 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:09:49 | Galgamuwa (Mee Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-10-31 11:09:46 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:06:49 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:06:22 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-10-31 11:06:17 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-10-31 11:06:03 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:05:40 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.065 |  |
| 2026-10-31 11:05:38 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-10-31 11:05:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:04:42 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:04:27 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:04:16 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-31 11:04:16 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:04:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.031 |  |
| 2026-10-31 11:03:49 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:03:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.056 |  |
| 2026-10-31 11:03:30 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-10-31 11:03:30 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.074 |  |
| 2026-10-31 11:03:20 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:03:19 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:03:08 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.036 |  |
| 2026-10-31 11:03:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:03:04 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-10-31 11:03:02 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-10-31 11:02:55 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-10-31 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.080 |  |
| 2026-10-31 11:02:29 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:02:19 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:02:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:01:47 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.062 |  |
| 2026-10-31 11:01:42 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-10-31 11:01:18 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:01:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.050 |  |
| 2026-10-31 11:01:01 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | 0.000 |  |
| 2026-10-31 11:00:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:00:46 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-10-31 11:00:39 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:00:36 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 11:01:01 | Thalgahagoda (Nilwala Ganga) | 1.66 | 🟡 Alert | 0.000 |  |
| 2026-10-31 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.080 |  |
| 2026-10-31 11:06:17 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-10-31 11:00:36 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 11:02:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:02:29 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:16:10 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:04:27 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:03:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:06:49 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:00:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:03:19 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:04:42 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:09:46 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:05:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:03:49 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-31 11:09:49 | Galgamuwa (Mee Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-10-31 11:06:03 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:04:16 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:03:20 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:02:19 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-31 11:03:02 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-10-31 11:02:55 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-10-31 11:03:04 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-10-31 11:05:38 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-10-31 11:18:14 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | -0.025 |  |
| 2026-10-31 11:00:46 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-10-31 11:06:22 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-10-31 11:04:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.031 |  |
| 2026-10-31 11:03:08 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.036 |  |
| 2026-10-31 11:03:30 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-10-31 11:04:16 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-31 11:01:42 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-10-31 11:01:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.050 |  |
| 2026-10-31 11:03:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.056 |  |
| 2026-10-31 11:01:47 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.062 |  |
| 2026-10-31 11:05:40 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.065 |  |
| 2026-10-31 11:03:30 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)