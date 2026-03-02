# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_11:06:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,102 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 11:06:33 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:06:17 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:06:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:05:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-02 11:05:32 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:05:09 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.039 |  |
| 2026-03-02 11:04:29 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-02 11:04:14 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:04:08 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:03:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-02 11:03:21 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 11:03:15 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-03-02 11:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 11:02:44 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:38 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-03-02 11:02:31 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:31 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.014 |  |
| 2026-03-02 11:02:23 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:21 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:01 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:58 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-02 11:01:18 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:18 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-02 11:01:14 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-02 11:01:13 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:01:12 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:08 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 11:01:07 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:00:54 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-02 11:00:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:00:22 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.066 |  |
| 2026-03-02 11:00:20 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:38:40 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.005 |  |
| 2026-03-02 10:28:21 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:26:22 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:19:35 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.014 |  |
| 2026-03-02 10:18:40 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-02 10:17:02 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.013 |  |
| 2026-03-02 10:11:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 11:01:14 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-02 11:01:18 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-02 11:04:29 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-02 11:03:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-02 11:03:21 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 11:01:08 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 11:05:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-02 11:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 11:06:17 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:00:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:04:08 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:06:33 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:01 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:04:14 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:18 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:06:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:44 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:31 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:00:20 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:21 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:02:23 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:06:10 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:06:51 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:09:04 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:05:32 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:12 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 10:38:40 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.005 |  |
| 2026-03-02 11:01:13 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:01:07 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:01:58 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-02 11:03:15 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-03-02 11:02:31 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.014 |  |
| 2026-03-02 11:02:38 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-03-02 11:00:54 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-02 11:05:09 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.039 |  |
| 2026-03-02 10:06:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.049 |  |
| 2026-03-02 11:00:22 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.066 |  |
| 2026-03-02 10:06:07 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)