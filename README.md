# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_19:14:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 19:14:25 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:14:09 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.017 |  |
| 2026-05-02 19:13:21 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:10:04 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.088 |  |
| 2026-05-02 19:09:19 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-02 19:08:29 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:08:17 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.011 |  |
| 2026-05-02 19:08:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-05-02 19:07:51 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 19:07:33 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:07:28 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-02 19:06:55 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:06:33 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:05:55 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-05-02 19:05:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-02 19:04:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-02 19:04:48 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-05-02 19:04:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.058 |  |
| 2026-05-02 19:04:15 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-02 19:04:03 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:02:42 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-02 19:02:38 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-02 19:02:18 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-05-02 19:02:16 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-05-02 19:02:12 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:02:10 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-05-02 19:01:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:01:38 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-02 19:01:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:48 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:42 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.014 |  |
| 2026-05-02 19:00:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:13 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:59:43 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 19:02:18 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 19:07:28 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-02 19:04:15 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-02 19:09:19 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-02 18:20:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 19:02:38 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-02 19:05:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-02 19:07:51 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 19:07:33 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:13 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:01:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:14:25 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:13:21 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:08:29 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:48 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:00:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:02:12 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:06:55 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:01:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:05:55 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-05-02 19:02:42 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-02 19:04:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:11:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-02 19:01:38 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-02 19:02:16 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-05-02 19:08:17 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.011 |  |
| 2026-05-02 19:00:42 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.014 |  |
| 2026-05-02 19:14:09 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.017 |  |
| 2026-05-02 19:02:10 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-05-02 18:59:43 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.023 |  |
| 2026-05-02 19:08:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-05-02 19:04:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.058 |  |
| 2026-05-02 19:04:48 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-05-02 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.070 |  |
| 2026-05-02 19:10:04 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)