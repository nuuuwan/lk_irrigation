# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_14:17:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 14:17:03 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:12:28 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.054 |  |
| 2026-02-14 14:11:39 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:11:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-14 14:09:54 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.019 |  |
| 2026-02-14 14:08:04 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:06:51 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:06:30 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 14:06:02 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.046 |  |
| 2026-02-14 14:06:01 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 14:05:22 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:04:46 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-02-14 14:04:29 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 14:04:26 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:04:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:03:41 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:22 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:22 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:12 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:02:53 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:02:42 | Padiyathalawa (Maduru Oya) | 3.46 | 🟢 Normal | 0.664 | 🔺 Rising |
| 2026-02-14 14:02:41 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.059 |  |
| 2026-02-14 14:02:38 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-14 14:02:36 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 14:02:28 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-14 14:02:26 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:02:11 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:02:08 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:02:06 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:02:00 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:01:51 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 14:01:23 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:01:03 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:00:39 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:00:05 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 14:02:42 | Padiyathalawa (Maduru Oya) | 3.46 | 🟢 Normal | 0.664 | 🔺 Rising |
| 2026-02-14 14:02:38 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-14 14:02:28 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-14 14:02:36 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 14:06:30 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 13:05:25 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 14:11:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-14 14:01:51 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 14:04:29 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 14:06:01 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 14:02:11 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:17:03 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:11:39 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:02:06 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:05:28 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:05:22 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:02:53 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:22 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:41 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:08:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:08:04 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:04:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:04:26 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:12 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:00:39 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:03:22 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:01:03 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:14:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:06:51 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 14:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:02:08 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:02:26 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:02:00 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:01:23 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-14 14:09:54 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.019 |  |
| 2026-02-14 14:04:46 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-02-14 14:06:02 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.046 |  |
| 2026-02-14 14:12:28 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.054 |  |
| 2026-02-14 14:02:41 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)