# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_00:13:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,363 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 00:13:11 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:10:31 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-05 00:09:12 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:09:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -90.000 |  |
| 2026-04-05 00:08:59 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -90.000 |  |
| 2026-04-05 00:08:54 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:07:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-05 00:06:57 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.049 |  |
| 2026-04-05 00:06:17 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 00:05:55 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-05 00:05:49 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-04-05 00:05:45 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:05:09 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:04:51 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:04:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:04:01 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-04-05 00:03:33 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.058 |  |
| 2026-04-05 00:03:25 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-05 00:03:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-05 00:02:59 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.131 |  |
| 2026-04-05 00:02:48 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.042 |  |
| 2026-04-05 00:02:48 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.046 |  |
| 2026-04-05 00:02:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-05 00:02:33 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:02:27 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:02:19 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:02:11 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 00:02:00 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:01:49 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 23:57:14 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-04-04 23:41:59 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.331 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 23:41:59 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-04-05 00:07:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-05 00:02:11 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 00:06:17 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 23:02:14 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 00:04:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-04 23:00:25 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:13:11 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:02:27 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:02:19 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:05:45 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:08:54 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:02:00 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 23:03:35 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:09:12 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:01:49 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:05:09 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-04 23:02:26 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.005 |  |
| 2026-04-05 00:05:49 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-04-05 00:10:31 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-05 00:02:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-05 00:03:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-04 23:57:14 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-04-04 23:18:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-04-05 00:03:25 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-05 00:05:55 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 00:04:01 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-04-05 00:02:48 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.042 |  |
| 2026-04-05 00:02:48 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.046 |  |
| 2026-04-05 00:06:57 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.049 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-05 00:03:33 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.058 |  |
| 2026-04-05 00:02:59 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.131 |  |
| 2026-04-04 22:09:36 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.134 |  |
| 2026-04-05 00:09:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)