# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_02:01:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,452 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 02:01:11 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-05-02 02:00:53 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 01:42:54 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.013 |  |
| 2026-05-02 01:13:31 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:13:29 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:13:28 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:08:35 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 01:01:54 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-05-02 01:03:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-02 01:00:59 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-02 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-02 01:02:36 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-02 02:00:53 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 01:03:42 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 00:01:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:16:36 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:04:53 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:13:31 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:01:55 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:12:57 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:05:44 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:01:52 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:02:31 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:04:01 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:01:18 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-02 01:02:43 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:37:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.006 |  |
| 2026-05-02 01:01:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-02 01:04:40 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-02 01:05:12 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-02 02:01:11 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-05-01 23:00:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-05-02 01:42:54 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.013 |  |
| 2026-05-02 01:03:40 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-05-02 01:03:15 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-05-02 01:02:21 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-05-02 01:02:46 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-05-02 01:07:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-05-01 23:13:38 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 01:08:35 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-05-02 00:02:00 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.069 |  |
| 2026-05-02 01:03:03 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.078 |  |
| 2026-05-02 00:01:27 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)