# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_01:21:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 01:21:59 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-04-26 01:21:34 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-26 01:10:04 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-26 01:08:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:07:27 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:07:17 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-04-26 01:06:32 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:05:46 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-04-26 01:05:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:04:39 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:04:24 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-26 01:04:03 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:03:51 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:03:48 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:03:36 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:03:13 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-04-26 01:02:43 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:21 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:02:16 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-26 01:02:07 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:02:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:00 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:00 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-26 01:01:53 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.021 |  |
| 2026-04-26 01:01:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:52 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:48 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:38 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:35 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-04-26 01:01:11 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-26 00:42:50 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-26 00:38:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 01:02:16 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-26 00:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-26 01:10:04 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-26 01:21:34 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-26 01:04:24 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-26 01:03:36 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:52 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:38 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:43 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 00:01:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:03:51 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:08:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:00 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:04:39 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:48 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:03:48 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:11 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-26 00:11:54 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-04-26 01:21:59 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-04-26 01:07:17 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-04-26 01:06:32 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:07:27 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:04:03 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:02:07 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:02:21 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-26 01:05:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-26 00:00:44 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-26 01:02:00 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-26 01:01:35 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-04-26 01:03:13 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-26 01:01:53 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.021 |  |
| 2026-04-26 01:05:46 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 22:11:27 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)