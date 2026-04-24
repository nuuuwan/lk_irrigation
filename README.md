# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_04:15:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 04:15:47 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-04-25 04:13:51 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:12:09 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:11:30 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:11:28 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-04-25 04:10:39 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:09:37 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.035 |  |
| 2026-04-25 04:07:59 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-04-25 04:06:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:06:10 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-25 04:05:50 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -3.789 |  |
| 2026-04-25 04:05:40 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:05:31 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -3.789 |  |
| 2026-04-25 04:05:28 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-25 04:05:23 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:04:46 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -3.789 |  |
| 2026-04-25 04:04:42 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 04:04:15 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-25 04:04:08 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:04:08 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-25 04:03:56 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-04-25 04:03:40 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:03:39 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:03:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:03:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:03:00 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-25 04:02:28 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-04-25 04:02:17 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:01:43 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:01:42 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:01:16 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.040 |  |
| 2026-04-25 04:01:07 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-25 04:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:00:50 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:00:45 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:47:53 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 03:43:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 04:03:56 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-04-25 04:03:00 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-25 03:47:53 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 04:01:07 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 04:04:42 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 04:00:45 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:00:50 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:03:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:01:43 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:13:51 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:02:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:11:30 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:03:40 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:00:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:06:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:05:23 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:04:08 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:12:09 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:05:40 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:01:42 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:11:28 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-04-25 03:03:52 | Katharagama (Menik Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-04-25 04:04:08 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-25 04:05:28 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-25 04:04:15 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-25 04:15:47 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-04-25 03:16:58 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-04-25 04:06:10 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-25 03:05:50 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.028 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-25 04:07:59 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-04-25 04:02:28 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-04-25 04:09:37 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.035 |  |
| 2026-04-25 04:01:16 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.040 |  |
| 2026-04-25 02:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.083 |  |
| 2026-04-25 04:05:50 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -3.789 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)