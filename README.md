# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_05:29:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,307 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 05:29:33 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-11-14 05:27:26 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | -0.024 |  |
| 2026-11-14 05:17:03 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.052 |  |
| 2026-11-14 05:14:27 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-14 05:12:55 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.044 |  |
| 2026-11-14 05:12:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-11-14 05:11:29 | Moraketiya (Walawe Ganga) | 2.85 | 🟢 Normal | -0.023 |  |
| 2026-11-14 05:09:50 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-11-14 05:08:02 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.042 |  |
| 2026-11-14 05:07:40 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-11-14 05:07:08 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -36.000 |  |
| 2026-11-14 05:07:07 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -36.000 |  |
| 2026-11-14 05:06:31 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:05:40 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.679 |  |
| 2026-11-14 05:05:31 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-11-14 05:05:21 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 05:05:05 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.074 |  |
| 2026-11-14 05:04:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.060 |  |
| 2026-11-14 05:04:06 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.019 |  |
| 2026-11-14 05:03:52 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:03:45 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.040 |  |
| 2026-11-14 05:03:40 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.010 |  |
| 2026-11-14 05:03:35 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-11-14 05:03:26 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-11-14 05:03:01 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.679 |  |
| 2026-11-14 05:02:58 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:48 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:02:39 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:19 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | -0.062 |  |
| 2026-11-14 05:02:18 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:11 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | -0.021 |  |
| 2026-11-14 05:02:09 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.080 |  |
| 2026-11-14 05:01:38 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 05:14:27 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-14 05:02:11 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | -0.021 |  |
| 2026-11-14 05:27:26 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | -0.024 |  |
| 2026-11-14 05:04:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.060 |  |
| 2026-11-14 05:00:09 | Weraganthota (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-11-14 05:05:21 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 05:02:58 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:00:18 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:39 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:02:12 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:18 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:04:06 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:06:31 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:03:52 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:03:06 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:04:44 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-11-14 05:05:31 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-11-14 05:03:35 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-11-14 05:03:26 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-11-14 05:03:40 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.010 |  |
| 2026-11-14 05:09:50 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-11-14 05:29:33 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-11-14 05:07:40 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-11-14 05:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.019 |  |
| 2026-11-14 05:02:48 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:01:38 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:11:29 | Moraketiya (Walawe Ganga) | 2.85 | 🟢 Normal | -0.023 |  |
| 2026-11-14 05:12:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 05:03:45 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.040 |  |
| 2026-11-14 05:08:02 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.042 |  |
| 2026-11-14 05:12:55 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.044 |  |
| 2026-11-14 05:17:03 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.052 |  |
| 2026-11-14 05:02:19 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | -0.062 |  |
| 2026-11-14 05:05:05 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.074 |  |
| 2026-11-14 05:02:09 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.080 |  |
| 2026-11-14 05:05:40 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.679 |  |
| 2026-11-14 05:07:08 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)