# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_16:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 16:13:02 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-04-25 16:09:05 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-25 16:08:46 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-04-25 16:08:02 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-25 16:07:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:06:10 | Katharagama (Menik Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-04-25 16:06:08 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.032 |  |
| 2026-04-25 16:05:59 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:05:59 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.019 |  |
| 2026-04-25 16:05:45 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:05:13 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:04:33 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:04:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:59 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:03:52 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:03:49 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:03:30 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:24 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:03 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-04-25 16:02:57 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-25 16:02:51 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-04-25 16:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-04-25 16:02:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:57 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:49 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-04-25 16:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:32 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:26 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:21 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:11 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:00:58 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:00:44 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:00:27 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:00:09 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 16:02:57 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-25 15:23:15 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-25 16:09:05 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-25 16:08:02 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-25 16:01:32 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:57 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:00:27 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:05:59 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:03:52 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:05:13 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:04:33 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:07:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:26 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:03:49 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:03:59 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:02:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:21 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:01:11 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 16:13:02 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-04-25 16:05:45 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:24 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:00:44 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:03:30 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:00:58 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:04:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-25 16:00:09 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-04-25 16:08:46 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-04-25 16:05:59 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.019 |  |
| 2026-04-25 16:02:51 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-04-25 16:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-04-25 16:06:10 | Katharagama (Menik Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-04-25 16:06:08 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.032 |  |
| 2026-04-25 16:03:03 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-04-25 16:01:49 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-04-25 15:05:33 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)