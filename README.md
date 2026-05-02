# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_16:19:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 16:19:41 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.016 |  |
| 2026-05-02 16:19:10 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-02 16:15:18 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-02 16:12:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.079 |  |
| 2026-05-02 16:09:45 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:09:22 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.057 |  |
| 2026-05-02 16:09:06 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-05-02 16:08:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 16:15:18 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-02 16:04:43 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-02 16:19:10 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-02 16:03:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:04:45 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:01:41 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:01:10 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:03:14 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:09:45 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:04:31 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:01:45 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:06:57 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:03:07 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:02:54 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:03:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:04:10 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:04:20 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 16:01:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 15:06:18 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.005 |  |
| 2026-05-02 16:09:06 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-05-02 16:04:51 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-02 16:03:39 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-02 16:01:44 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-02 16:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-02 16:01:32 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-02 16:03:56 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-02 16:02:01 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-05-02 16:01:51 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-05-02 16:19:41 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.016 |  |
| 2026-05-02 16:02:42 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-05-02 16:02:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-05-02 16:03:44 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-05-02 16:01:06 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.030 |  |
| 2026-05-02 16:02:35 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-02 16:08:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.039 |  |
| 2026-05-02 16:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-05-02 16:02:42 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.041 |  |
| 2026-05-02 16:09:22 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.057 |  |
| 2026-05-02 16:12:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)