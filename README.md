# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_11:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 11:03:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:23 | Hanwella (Kelani Ganga) | 3.05 | 🟢 Normal | -0.040 |  |
| 2026-10-30 11:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:06 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:35 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-30 11:02:34 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:30 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-10-30 11:02:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:02:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:02:08 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:02:08 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:02:07 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:01:45 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.078 |  |
| 2026-10-30 11:01:06 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.066 |  |
| 2026-10-30 11:00:47 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:00:44 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:00:41 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.032 |  |
| 2026-10-30 11:00:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.064 |  |
| 2026-10-30 11:00:14 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.040 |  |
| 2026-10-30 11:00:06 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 10:06:11 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 10:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-30 10:04:31 | Putupaula (Kalu Ganga) | 3.40 | 🟡 Alert | -0.019 |  |
| 2026-10-30 10:01:48 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.057 |  |
| 2026-10-30 11:02:35 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-30 09:02:51 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 11:02:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:02:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:02:07 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 10:00:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-30 11:02:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:54 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:34 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:09:56 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:09 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:08:11 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:00:47 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:06 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:06:11 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-10-30 11:00:44 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:00:06 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:02:08 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:02:08 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-30 10:04:58 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.011 |  |
| 2026-10-30 10:01:59 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-10-30 10:05:24 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-30 11:02:30 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-10-30 10:11:51 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.027 |  |
| 2026-10-30 11:00:41 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.032 |  |
| 2026-10-30 11:00:14 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.040 |  |
| 2026-10-30 11:03:23 | Hanwella (Kelani Ganga) | 3.05 | 🟢 Normal | -0.040 |  |
| 2026-10-30 10:06:32 | Baddegama (Gin Ganga) | 3.46 | 🟢 Normal | -0.042 |  |
| 2026-10-30 10:03:35 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.042 |  |
| 2026-10-30 11:00:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.064 |  |
| 2026-10-30 11:01:06 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.066 |  |
| 2026-10-30 11:01:45 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.078 |  |
| 2026-10-30 09:01:35 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)