# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_18:39:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 18:39:59 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-02 18:08:29 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:07:34 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:07:10 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:06:47 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:06:25 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 18:05:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-04-02 18:05:49 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-02 18:05:15 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 18:08:29 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-04-02 18:05:49 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-02 18:02:28 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-02 18:02:32 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-02 18:03:52 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-02 18:39:59 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-02 18:06:25 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 18:02:52 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:06:47 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:01:30 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:05:15 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:01:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:02:10 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:05:44 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:02:44 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:01:18 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:07:34 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:03:05 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:00:40 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:01:20 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:02:13 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:01:35 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:02:28 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:04:22 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:04:19 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:02:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:02:14 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:07:10 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:02:09 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-02 18:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-04-02 18:01:08 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-04-02 18:03:44 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.030 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-02 18:05:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-04-02 18:00:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.098 |  |
| 2026-04-02 18:01:26 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)