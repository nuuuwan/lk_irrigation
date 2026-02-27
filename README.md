# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_20:21:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 20:21:11 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:20:23 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:13:04 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:10:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-27 20:10:16 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:09:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-02-27 20:08:42 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:08:33 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.009 |  |
| 2026-02-27 20:07:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:07:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:07:15 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-27 20:06:02 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.041 |  |
| 2026-02-27 20:05:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:05:25 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-27 20:05:19 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 20:04:44 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:20 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:11 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-02-27 20:03:45 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:03:33 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-02-27 20:03:23 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-27 20:03:13 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:03:02 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:02:58 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 20:02:58 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-27 20:05:25 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-27 20:04:49 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 20:10:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-27 20:02:39 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-27 20:03:02 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:07:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:02:08 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:10:16 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:01:52 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:05:19 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:13:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:02:29 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:03:45 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:01:45 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:20 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:02:00 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:01:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:02:23 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:03:13 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:05:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:08:42 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:20:23 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:21:11 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:13:04 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:04:44 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:02:10 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:08:33 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.009 |  |
| 2026-02-27 20:03:33 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-02-27 20:07:15 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-27 20:01:21 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-02-27 20:01:51 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-27 20:04:11 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-02-27 20:03:23 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-27 20:09:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-02-27 18:05:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.028 |  |
| 2026-02-27 20:06:02 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)