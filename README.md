# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_11:12:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,023 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 11:12:08 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 11:10:27 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:10:15 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-10-30 11:09:54 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:09:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:09:07 | Baddegama (Gin Ganga) | 3.42 | 🟢 Normal | -0.038 |  |
| 2026-10-30 11:07:20 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.047 |  |
| 2026-10-30 11:07:20 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | -288.000 |  |
| 2026-10-30 11:07:19 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | -288.000 |  |
| 2026-10-30 11:07:00 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-10-30 11:06:27 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:06:25 | Panadugama (Nilwala Ganga) | 5.41 | 🟡 Alert | -0.028 |  |
| 2026-10-30 11:06:21 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:05:37 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:05:19 | Putupaula (Kalu Ganga) | 3.37 | 🟡 Alert | -0.030 |  |
| 2026-10-30 11:05:11 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:52 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:03:43 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 11:03:43 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-10-30 11:03:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:23 | Hanwella (Kelani Ganga) | 3.05 | 🟢 Normal | -0.040 |  |
| 2026-10-30 11:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:06 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:35 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-30 11:02:34 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:30 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-10-30 11:02:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
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
| 2026-10-30 11:12:08 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 10:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-30 11:06:25 | Panadugama (Nilwala Ganga) | 5.41 | 🟡 Alert | -0.028 |  |
| 2026-10-30 11:05:19 | Putupaula (Kalu Ganga) | 3.37 | 🟡 Alert | -0.030 |  |
| 2026-10-30 11:02:35 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-30 11:03:43 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 11:02:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:02:07 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 11:02:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:02:34 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:09 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:00:47 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:06 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:06:21 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:10:27 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:09:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 11:03:52 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:05:37 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:06:27 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:00:44 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:00:06 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:02:08 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:02:08 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-30 11:07:00 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-10-30 11:02:30 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-10-30 11:03:43 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-10-30 11:00:41 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.032 |  |
| 2026-10-30 11:09:07 | Baddegama (Gin Ganga) | 3.42 | 🟢 Normal | -0.038 |  |
| 2026-10-30 11:00:14 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.040 |  |
| 2026-10-30 11:03:23 | Hanwella (Kelani Ganga) | 3.05 | 🟢 Normal | -0.040 |  |
| 2026-10-30 11:10:15 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-10-30 11:07:20 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.047 |  |
| 2026-10-30 11:00:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.064 |  |
| 2026-10-30 11:01:06 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.066 |  |
| 2026-10-30 11:01:45 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.078 |  |
| 2026-10-30 11:07:20 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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