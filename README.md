# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_12:14:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,397 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 12:14:18 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 12:06:26 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-06-02 12:07:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-06-02 12:04:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-02 12:03:08 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-02 12:02:39 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 12:01:15 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 12:03:39 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 12:04:03 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:00:07 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:01:01 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:02:32 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:01:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:05:59 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:02:26 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:06:15 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:04:32 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:00:52 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:02:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:02:18 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:04:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:07:15 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:03:33 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:03:25 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:14:18 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:00:58 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-02 12:05:24 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-06-02 12:06:35 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-02 12:04:50 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-06-02 12:02:52 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-02 12:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-02 12:06:32 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-02 12:03:59 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-02 12:05:51 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:02:00 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-06-02 12:01:27 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-06-02 12:02:27 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-06-02 12:04:01 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-06-02 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2026-06-02 12:00:16 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)