# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_10:10:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,554 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 10:10:57 | Katharagama (Menik Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:10:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-04-25 10:10:08 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.104 |  |
| 2026-04-25 10:08:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:08:23 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-04-25 10:08:01 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 10:07:16 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:07:13 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:06:52 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:06:34 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-25 10:05:48 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:05:22 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:05:05 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.005 |  |
| 2026-04-25 10:04:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-25 10:03:48 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:03:27 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | -0.011 |  |
| 2026-04-25 10:03:24 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:02:52 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-04-25 10:02:49 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-04-25 10:02:45 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:02:35 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.060 |  |
| 2026-04-25 10:02:09 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:02:00 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:01:51 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:01:32 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:01:24 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.100 |  |
| 2026-04-25 10:01:18 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 10:00:59 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:00:39 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:00:28 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.063 |  |
| 2026-04-25 10:00:26 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.015 |  |
| 2026-04-25 10:00:14 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:00:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:20:02 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.015 |  |
| 2026-04-25 09:18:26 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.104 |  |
| 2026-04-25 09:18:24 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.104 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 10:04:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-25 09:04:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 10:08:01 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 10:02:09 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:00:59 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:02:35 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:10:57 | Katharagama (Menik Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:02:45 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:06:52 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:05:22 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:00:39 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:05:05 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.005 |  |
| 2026-04-25 10:08:23 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-04-25 10:06:34 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-25 10:03:24 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:05:48 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:01:18 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:03:48 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:08:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:02:00 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:00:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:01:51 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 10:02:49 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-04-25 10:03:27 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | -0.011 |  |
| 2026-04-25 10:00:26 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.015 |  |
| 2026-04-25 10:07:13 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:07:16 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:01:46 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:01:32 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:00:14 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.020 |  |
| 2026-04-25 10:10:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-04-25 09:09:12 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.037 |  |
| 2026-04-25 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.060 |  |
| 2026-04-25 10:02:52 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-04-25 10:00:28 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.063 |  |
| 2026-04-25 10:01:24 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.100 |  |
| 2026-04-25 10:10:08 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)