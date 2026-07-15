# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_09:13:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,761 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 09:13:50 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:11:24 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:09:02 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.009 |  |
| 2026-07-15 09:08:45 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-15 09:06:59 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-07-15 09:06:38 | Thalgahagoda (Nilwala Ganga) | 0.02 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-07-15 09:05:52 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:50 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:46 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:40 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:39 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | -0.033 |  |
| 2026-07-15 09:04:59 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:28 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:26 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-07-15 09:04:09 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-07-15 09:03:56 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:03:46 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-15 09:03:24 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.299 |  |
| 2026-07-15 09:03:12 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:03:12 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:03:06 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:03:02 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:02:58 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:02:44 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-15 09:02:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:02:24 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-15 09:02:23 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:02:19 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:02:12 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:02:12 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 09:01:22 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-07-15 09:01:16 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:01:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:01:00 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:25 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:15 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 09:06:59 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-07-15 09:04:09 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-07-15 09:08:45 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-15 09:02:44 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-15 09:03:46 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-15 09:02:24 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-15 09:02:12 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 09:00:15 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:52 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:01:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:11:24 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:02:58 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:03:12 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:03:02 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:50 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:01:00 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:28 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:40 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:01:16 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:26 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:13:50 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:59 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:05:46 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:03:12 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:04:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:00:25 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:02:23 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 09:09:02 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.009 |  |
| 2026-07-15 09:03:06 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:02:19 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:02:12 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-15 09:02:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-15 08:00:44 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-07-15 09:01:22 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-07-15 09:05:39 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | -0.033 |  |
| 2026-07-15 09:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-07-15 09:03:24 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)