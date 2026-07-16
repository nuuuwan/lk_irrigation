# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--17_04:28:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,340 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 04:28:04 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:27:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:13:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.018 |  |
| 2026-07-17 04:10:52 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:08:55 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:08:00 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:07:20 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-17 04:07:11 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-07-17 04:07:07 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:07:00 | Moraketiya (Walawe Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:05:03 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:04:15 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.119 |  |
| 2026-07-17 04:04:05 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-17 04:03:51 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:03:39 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-07-17 04:03:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-17 04:02:54 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:02:37 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:02:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-17 04:01:59 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.055 |  |
| 2026-07-17 04:01:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:41 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:35 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-17 04:01:23 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:13 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:10 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:00:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-17 04:00:37 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.044 |  |
| 2026-07-17 04:00:12 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-17 03:52:18 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 03:51:03 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 04:03:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-17 04:04:05 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-17 04:07:20 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-17 04:02:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-16 18:01:19 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 04:00:12 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:02:54 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:27:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:41 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 03:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-17 02:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:02:37 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 18:09:00 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:03:51 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-17 00:05:54 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:05:03 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:13 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:28:04 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 03:00:38 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:07:00 | Moraketiya (Walawe Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:10 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:07:07 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 03:02:18 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:08:55 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:10:52 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-16 18:01:35 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-17 03:06:58 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:08:00 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-17 01:05:26 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:01:23 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 04:00:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-17 04:03:39 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-07-17 04:07:11 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-07-17 04:01:35 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-17 04:13:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.018 |  |
| 2026-07-17 04:00:37 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.044 |  |
| 2026-07-17 04:01:59 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.055 |  |
| 2026-07-17 04:04:15 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)