# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_08:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,993 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 08:14:58 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2026-10-19 08:10:10 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.098 |  |
| 2026-10-19 08:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.037 |  |
| 2026-10-19 08:07:14 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.035 |  |
| 2026-10-19 08:06:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-19 08:06:40 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.053 |  |
| 2026-10-19 08:06:20 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 08:05:53 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:05:52 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-10-19 08:05:45 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:05:39 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-10-19 08:05:16 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-10-19 08:04:55 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.083 |  |
| 2026-10-19 08:04:44 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-10-19 08:04:39 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.022 |  |
| 2026-10-19 08:04:18 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-19 08:04:12 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-19 08:04:03 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 08:03:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:03:45 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:03:37 | Dunamale (Aththanagalu Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:03:14 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.071 |  |
| 2026-10-19 08:03:01 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:02:55 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:02:40 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.039 |  |
| 2026-10-19 08:02:20 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.048 |  |
| 2026-10-19 08:02:13 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:02:00 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2026-10-19 08:01:51 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.097 |  |
| 2026-10-19 08:01:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:01:35 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-19 08:01:34 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-10-19 08:01:24 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.034 |  |
| 2026-10-19 08:01:11 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 08:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:37:09 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.048 |  |
| 2026-10-19 07:33:10 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 08:04:03 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 08:06:40 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.053 |  |
| 2026-10-19 08:04:18 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-19 08:01:11 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 08:06:20 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 08:06:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-19 08:01:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:02:18 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:02:13 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-19 07:13:18 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:05:45 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:03:37 | Dunamale (Aththanagalu Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:03:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:04:12 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-19 07:02:07 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-19 08:01:35 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-19 08:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-19 08:01:34 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-10-19 08:04:44 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-10-19 08:05:52 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-10-19 08:02:55 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:03:45 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:05:53 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:03:01 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.020 |  |
| 2026-10-19 08:05:39 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-10-19 08:04:39 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.022 |  |
| 2026-10-19 08:01:24 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.034 |  |
| 2026-10-19 08:07:14 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.035 |  |
| 2026-10-19 08:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.037 |  |
| 2026-10-19 08:05:16 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-10-19 08:02:40 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.039 |  |
| 2026-10-19 08:02:00 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2026-10-19 08:02:20 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.048 |  |
| 2026-10-19 08:14:58 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2026-10-19 08:03:14 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.071 |  |
| 2026-10-19 07:00:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-10-19 08:04:55 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.083 |  |
| 2026-10-19 08:01:51 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.097 |  |
| 2026-10-19 08:10:10 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)