# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_10:29:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 10:29:12 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.044 |  |
| 2026-10-02 10:17:02 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:14:40 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-10-02 10:12:37 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.110 |  |
| 2026-10-02 10:09:12 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.101 |  |
| 2026-10-02 10:08:11 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.027 |  |
| 2026-10-02 10:08:03 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-10-02 10:07:30 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.028 |  |
| 2026-10-02 10:06:46 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:06:34 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.050 |  |
| 2026-10-02 10:06:29 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:05:22 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.038 |  |
| 2026-10-02 10:04:20 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-10-02 10:04:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:50 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:03:45 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:35 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-02 10:03:33 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 10:03:24 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:22 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-10-02 10:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:05 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 10:03:02 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.047 |  |
| 2026-10-02 10:03:01 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.120 |  |
| 2026-10-02 10:02:15 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 10:02:04 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.276 |  |
| 2026-10-02 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:48 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 10:01:29 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:20 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.060 |  |
| 2026-10-02 10:01:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.030 |  |
| 2026-10-02 10:01:17 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 10:00:52 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:00:52 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-02 10:00:46 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.399 |  |
| 2026-10-02 10:00:28 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 10:00:52 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-02 10:01:48 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 10:03:05 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 10:01:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 10:02:15 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 10:03:33 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 10:17:02 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:00:52 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:29 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:01:17 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:24 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:04:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:45 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:00:28 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:14:40 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-10-02 10:03:50 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:06:46 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:06:29 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:03:35 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-02 10:04:20 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-10-02 10:08:03 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-10-02 10:03:22 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-10-02 10:08:11 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.027 |  |
| 2026-10-02 10:07:30 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.028 |  |
| 2026-10-02 10:01:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.030 |  |
| 2026-10-02 10:05:22 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.038 |  |
| 2026-10-02 10:29:12 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.044 |  |
| 2026-10-02 10:03:02 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.047 |  |
| 2026-10-02 10:06:34 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.050 |  |
| 2026-10-02 10:01:20 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.060 |  |
| 2026-10-02 10:09:12 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.101 |  |
| 2026-10-02 10:12:37 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.110 |  |
| 2026-10-02 10:03:01 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.120 |  |
| 2026-10-02 10:02:04 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.276 |  |
| 2026-10-02 10:00:46 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.399 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)