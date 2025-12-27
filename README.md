# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_08:02:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,080 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 08:02:17 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:01:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 08:01:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-27 08:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:01:17 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:43 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:00:41 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:31 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:10 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:07 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:18:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2025-12-27 07:15:14 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2025-12-27 07:14:03 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:13:36 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:12:42 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:12:28 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.084 |  |
| 2025-12-27 07:10:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:07:11 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-27 07:07:09 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 07:06:55 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2025-12-27 07:05:45 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.012 |  |
| 2025-12-27 07:05:40 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:05:16 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.047 |  |
| 2025-12-27 07:05:10 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:04:40 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-27 07:04:24 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:04:18 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 07:07:11 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-27 07:04:40 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-27 07:00:14 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-27 07:03:20 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-27 08:01:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 07:07:09 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 06:07:12 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.004 |  |
| 2025-12-27 07:02:52 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:07 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:04:18 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:12:28 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:02:59 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:05:10 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:14:03 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:10 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:01:17 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:41 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:01:38 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:10:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:04:24 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:31 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:13:36 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:01:24 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:01:47 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:18:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2025-12-27 08:02:17 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:00:43 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 07:03:20 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-27 07:02:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-27 07:05:45 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.012 |  |
| 2025-12-27 08:01:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-27 07:01:58 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2025-12-27 07:06:55 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2025-12-27 07:02:01 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2025-12-27 07:01:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-27 07:05:16 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.047 |  |
| 2025-12-27 07:03:25 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.059 |  |
| 2025-12-27 07:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)