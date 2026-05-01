# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_03:25:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,514 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 03:25:12 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.055 |  |
| 2026-05-02 03:19:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:19:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:17:20 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-02 03:16:32 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.005 |  |
| 2026-05-02 03:16:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:13:51 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 03:11:45 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.063 |  |
| 2026-05-02 03:10:04 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -216.000 |  |
| 2026-05-02 03:10:03 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -216.000 |  |
| 2026-05-02 03:08:10 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-05-02 03:07:55 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:46 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:45 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:10 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-05-02 03:05:10 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:09 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-05-02 03:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-02 03:04:46 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:04:31 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:04:16 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-02 03:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.004 |  |
| 2026-05-02 03:04:12 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-05-02 03:04:00 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:03:58 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:03:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-05-02 03:03:43 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 03:03:08 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.043 |  |
| 2026-05-02 03:03:04 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 03:02:52 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:34 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:26 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 03:02:08 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:04 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:00 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.060 |  |
| 2026-05-02 03:01:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-02 03:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:00:19 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-02 02:41:01 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.184 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 03:05:10 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-05-02 03:08:10 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-05-02 03:03:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-05-02 03:17:20 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-02 03:00:19 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-02 03:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-02 03:03:04 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 03:02:26 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 03:13:51 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 03:03:43 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 03:01:18 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-02 03:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:07:55 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:04:00 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:03:58 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:46 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:19:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:52 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:16:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:04 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:10 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:05:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:02:34 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:19:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:04:31 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 03:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.004 |  |
| 2026-05-02 03:16:32 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.005 |  |
| 2026-05-02 02:04:05 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-02 03:04:16 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 02:23:43 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.042 |  |
| 2026-05-02 03:03:08 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.043 |  |
| 2026-05-02 03:04:12 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-05-02 03:25:12 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.055 |  |
| 2026-05-02 03:02:00 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.060 |  |
| 2026-05-02 03:11:45 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.063 |  |
| 2026-05-02 03:10:04 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)