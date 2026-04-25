# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_21:28:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,981 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 21:28:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.008 |  |
| 2026-04-25 21:14:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-25 21:13:32 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-04-25 21:11:16 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:08:46 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:08:16 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:07:09 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:07:01 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.031 |  |
| 2026-04-25 21:06:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:06:52 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:06:01 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:05:33 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:05:27 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:05:15 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:05:08 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:04:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:04:16 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-25 21:04:08 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:04:06 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:03:53 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-04-25 21:03:51 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:03:40 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-25 21:03:33 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:03:10 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:02:32 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-25 21:02:29 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:02:25 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:02:11 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:02:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:02:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:01:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:01:15 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2026-04-25 21:01:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:01:05 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 21:00:39 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 21:00:32 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 21:14:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-25 21:00:39 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 21:04:16 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-25 21:03:40 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-25 21:01:05 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 21:05:15 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:06:52 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:02:25 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:01:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:06:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:02:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:03:33 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:04:06 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:06:01 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:00:32 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:04:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:05:08 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:05:27 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:08:46 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:07:09 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:08:16 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:11:16 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:28:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.008 |  |
| 2026-04-25 21:04:08 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:05:33 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:01:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:03:51 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:02:29 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:02:11 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-25 21:02:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 21:02:32 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 21:03:53 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-04-25 21:07:01 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.031 |  |
| 2026-04-25 21:13:32 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-04-25 21:01:15 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)