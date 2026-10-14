# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_17:07:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,822 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 17:07:08 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-10-14 17:07:02 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-10-14 17:07:02 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-10-14 17:06:40 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -5.714 |  |
| 2026-10-14 17:06:26 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-10-14 17:06:08 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | -0.174 |  |
| 2026-10-14 17:06:01 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:05:37 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -5.714 |  |
| 2026-10-14 17:05:08 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-14 17:05:08 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 17:04:53 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-14 17:04:40 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-14 17:04:37 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-14 17:04:34 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-10-14 17:04:30 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 17:04:16 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-14 17:04:15 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-10-14 17:04:12 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | -0.023 |  |
| 2026-10-14 17:02:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:02:50 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 17:02:45 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 17:02:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:02:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:01:53 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 17:01:15 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:01:04 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:01:02 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 17:00:59 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:00:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:00:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:33:16 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 16:01:13 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 16:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-14 16:01:57 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.067 |  |
| 2026-10-14 17:06:08 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | -0.174 |  |
| 2026-10-14 16:06:42 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 1.083 | 🔺 Rising |
| 2026-10-14 17:07:08 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-10-14 17:07:02 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-10-14 17:04:37 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-14 17:04:53 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-14 16:04:18 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-14 17:05:08 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-14 17:04:40 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-14 17:02:45 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 17:05:08 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 17:04:16 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-14 16:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 17:01:02 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 17:02:50 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 17:01:53 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 17:02:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:00:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:00:59 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:33:16 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:04:59 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:01:04 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:06:01 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:00:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:02:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:02:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:06:26 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-10-14 16:01:12 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-14 17:04:30 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 17:04:12 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | -0.023 |  |
| 2026-10-14 17:07:02 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-10-14 17:04:34 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-10-14 17:04:15 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-10-14 16:01:46 | Rathnapura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.073 |  |
| 2026-10-14 16:03:40 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.100 |  |
| 2026-10-14 17:06:40 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -5.714 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)