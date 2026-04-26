# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_10:25:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,456 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 10:25:12 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.007 |  |
| 2026-04-26 10:17:16 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-04-26 10:14:05 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:11:23 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.009 |  |
| 2026-04-26 10:11:08 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-04-26 10:09:12 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:08:31 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:08:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-04-26 10:07:23 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:06:25 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.030 |  |
| 2026-04-26 10:06:08 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.101 |  |
| 2026-04-26 10:05:40 | Katharagama (Menik Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:05:40 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:05:25 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.009 |  |
| 2026-04-26 10:04:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:04:54 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-04-26 10:04:19 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.012 |  |
| 2026-04-26 10:04:15 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:04:09 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.034 |  |
| 2026-04-26 10:03:54 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:03:31 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:03:20 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:52 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:40 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.060 |  |
| 2026-04-26 10:02:08 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:01 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:48 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:47 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.073 |  |
| 2026-04-26 10:01:30 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:23 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.424 |  |
| 2026-04-26 10:01:10 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:00:59 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.021 |  |
| 2026-04-26 10:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:00:38 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 09:02:52 | Urawa (Nilwala Ganga) | 4.00 | 🟠 Minor Flood | 1.986 | 🔺 Rising |
| 2026-04-26 10:00:38 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 10:02:01 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:09:12 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:04:15 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:52 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:03:20 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:14:05 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:40 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:30 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:05:40 | Katharagama (Menik Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:05:40 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:03:54 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:48 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:01:10 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:02:08 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-26 10:25:12 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.007 |  |
| 2026-04-26 10:11:23 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.009 |  |
| 2026-04-26 10:05:25 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.009 |  |
| 2026-04-26 10:03:31 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:07:23 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:04:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:08:31 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-26 10:04:19 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.012 |  |
| 2026-04-26 10:11:08 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-04-26 10:17:16 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-04-26 10:00:59 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.021 |  |
| 2026-04-26 10:04:54 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-04-26 10:06:25 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.030 |  |
| 2026-04-26 10:08:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-04-26 10:04:09 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.034 |  |
| 2026-04-26 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.060 |  |
| 2026-04-26 10:01:47 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.073 |  |
| 2026-04-26 10:06:08 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.101 |  |
| 2026-04-26 10:01:23 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.424 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)