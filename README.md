# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_13:46:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 13:46:33 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:15:52 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:12:31 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-01-05 13:11:48 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:11:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-05 13:09:42 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:08:09 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:06:47 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:06:46 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:06:34 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:06:14 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.256 |  |
| 2026-01-05 13:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-01-05 13:06:09 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:05:46 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:05:37 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 13:04:27 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 13:04:11 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:04:08 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-05 13:03:50 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:03:46 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:03:34 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:59 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:52 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:02:48 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:35 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:02:33 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 13:02:26 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-05 13:02:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:18 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 13:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:01:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:01:26 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-01-05 13:01:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:46 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:45 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:41 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:28 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:09 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 13:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-01-05 13:04:27 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 13:11:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-05 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 13:02:26 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-05 13:05:37 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 13:02:33 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 13:02:48 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:18 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:06:09 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:06:46 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:46 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:46:33 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:03:34 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:11:48 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:03:46 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:41 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:28 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:04:11 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:06:34 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:00:45 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:15:52 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:01:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:09:42 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:02:59 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:12:31 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-01-05 13:04:08 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-05 13:08:09 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:02:52 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:03:50 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:06:47 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:00:09 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:05:46 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.010 |  |
| 2026-01-05 13:02:35 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-05 12:20:32 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-01-05 13:01:26 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-01-05 12:01:43 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-01-05 13:06:14 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)