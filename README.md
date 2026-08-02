# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_19:19:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,147 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 19:19:26 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-02 19:15:30 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-02 19:10:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-02 19:10:15 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-02 19:09:59 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 19:09:40 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-08-02 19:09:30 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-02 19:08:46 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-02 19:08:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.173 |  |
| 2026-08-02 19:08:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:07:54 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.027 |  |
| 2026-08-02 19:07:37 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-02 19:06:45 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.019 |  |
| 2026-08-02 19:05:47 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.033 |  |
| 2026-08-02 19:05:09 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-08-02 19:05:09 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-02 19:04:51 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 19:03:49 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:03:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:02:58 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-02 19:02:49 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-02 19:02:42 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-08-02 19:02:20 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-08-02 19:02:00 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-08-02 19:01:56 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.040 |  |
| 2026-08-02 19:01:54 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:32 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:30 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-08-02 19:01:28 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:28 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:00:14 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:59:34 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 19:02:00 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-08-02 19:02:42 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-08-02 19:02:58 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-02 19:07:37 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-02 19:05:09 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-02 18:02:06 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-02 19:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-02 19:19:26 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-02 19:15:30 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-02 19:08:46 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-02 19:10:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-02 19:09:59 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 19:10:15 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-02 19:04:51 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 19:00:14 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:03:49 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:28 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:54 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:59:34 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:32 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:08:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:03:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:01:28 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:02:49 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 19:09:40 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-08-02 19:09:30 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-02 19:06:45 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.019 |  |
| 2026-08-02 19:05:09 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-08-02 19:01:30 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-02 19:07:54 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.027 |  |
| 2026-08-02 19:02:20 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-08-02 19:05:47 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.033 |  |
| 2026-08-02 19:01:56 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.040 |  |
| 2026-08-02 19:08:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)