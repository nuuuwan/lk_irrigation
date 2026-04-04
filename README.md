# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_18:08:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,151 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 18:08:14 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 18:07:02 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:06:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-04 18:05:27 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-04 18:05:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.156 |  |
| 2026-04-04 18:04:37 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-04 18:04:05 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-04-04 18:03:55 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.057 |  |
| 2026-04-04 18:03:41 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.042 |  |
| 2026-04-04 18:03:34 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-04 18:03:32 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-04 18:03:31 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:28 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.043 |  |
| 2026-04-04 18:03:22 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:21 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:21 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-04 18:03:18 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:15 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-04 18:02:56 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-04-04 18:02:51 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-04 18:02:51 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-04 18:02:47 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-04-04 18:02:38 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 18:02:34 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.107 |  |
| 2026-04-04 18:02:20 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-04-04 18:02:06 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 18:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 18:01:45 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:01:42 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:01:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-04 18:01:05 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-04 18:01:00 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 18:00:58 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-04-04 18:00:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:00:13 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 18:04:05 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-04-04 18:03:32 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-04 18:03:21 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-04 18:04:37 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-04 18:03:34 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-04 18:02:06 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 18:08:14 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 18:06:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-04 18:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 18:03:15 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-04 18:02:38 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 18:05:27 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-04 18:01:00 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 18:01:42 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:01:05 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:21 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:22 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:01:45 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:02:20 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:18 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:07:02 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:00:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:03:31 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-04 18:02:56 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-04-04 18:00:13 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-04 18:01:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-04 18:02:51 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-04 18:02:51 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-04 18:00:58 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-04-04 18:02:47 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-04 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-04-04 18:03:41 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.042 |  |
| 2026-04-04 18:03:28 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.043 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-04 18:03:55 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.057 |  |
| 2026-04-04 18:02:34 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.107 |  |
| 2026-04-04 18:05:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)