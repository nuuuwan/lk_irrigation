# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_14:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 14:16:20 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.025 |  |
| 2026-10-19 14:13:46 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:12:59 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.033 |  |
| 2026-10-19 14:11:48 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 14:10:13 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-10-19 14:09:45 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.109 |  |
| 2026-10-19 14:07:55 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-10-19 14:07:43 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-10-19 14:07:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.72 | 🟢 Normal | -0.035 |  |
| 2026-10-19 14:07:24 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.028 |  |
| 2026-10-19 14:06:59 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:06:53 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-19 14:06:39 | Panadugama (Nilwala Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-10-19 14:06:23 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:06:22 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:06:07 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:05:23 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:04:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:04:23 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.028 |  |
| 2026-10-19 14:04:17 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:03:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:03:11 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-10-19 14:03:10 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.060 |  |
| 2026-10-19 14:03:08 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.082 |  |
| 2026-10-19 14:02:59 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 14:02:56 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-10-19 14:02:48 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:02:46 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 14:02:37 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:02:09 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-10-19 14:01:48 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:01:34 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-19 14:01:26 | Ellagawa (Kalu Ganga) | 7.03 | 🟢 Normal | -0.072 |  |
| 2026-10-19 14:01:00 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.149 |  |
| 2026-10-19 14:00:56 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.031 |  |
| 2026-10-19 14:00:52 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-10-19 14:00:24 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:00:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 14:11:48 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 14:06:39 | Panadugama (Nilwala Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-10-19 14:02:46 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 14:02:59 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 14:03:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 13:05:58 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:01:48 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:05:23 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:06:07 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:00:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:06:23 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:06:59 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:13:46 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-19 14:10:13 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-10-19 14:07:43 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-10-19 14:06:53 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-19 14:02:37 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:04:17 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:00:24 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:04:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:02:48 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-19 14:02:56 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-10-19 14:00:52 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-10-19 14:07:55 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-10-19 14:01:34 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-19 14:03:11 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-10-19 14:16:20 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.025 |  |
| 2026-10-19 14:07:24 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.028 |  |
| 2026-10-19 14:04:23 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.028 |  |
| 2026-10-19 14:02:09 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-10-19 14:00:56 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.031 |  |
| 2026-10-19 14:12:59 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.033 |  |
| 2026-10-19 14:07:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.72 | 🟢 Normal | -0.035 |  |
| 2026-10-19 14:03:10 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.060 |  |
| 2026-10-19 14:01:26 | Ellagawa (Kalu Ganga) | 7.03 | 🟢 Normal | -0.072 |  |
| 2026-10-19 14:03:08 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.082 |  |
| 2026-10-19 14:09:45 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.109 |  |
| 2026-10-19 14:01:00 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)