# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_10:01:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,758 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:51 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.061 |  |
| 2026-02-23 10:01:02 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:40 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:36 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:22 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:59:26 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:21:36 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:09:53 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.017 |  |
| 2026-02-23 09:09:17 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-02-23 09:08:12 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:07:06 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:06:42 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-23 09:06:34 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-02-23 09:06:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 09:01:45 | Manampitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-23 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-23 09:02:37 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-23 09:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 09:01:00 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 09:01:47 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:40 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:08:12 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:03:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:07:06 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:01:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:02:46 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:02:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:05:29 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 10:00:36 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:08 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 09:09:17 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-02-23 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:03:08 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:02:14 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:01:02 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-23 10:00:22 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-23 09:06:34 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-02-23 09:09:53 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.017 |  |
| 2026-02-23 09:06:12 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-02-23 09:02:40 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-02-23 09:02:18 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-02-23 09:06:42 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-02-23 09:01:57 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-02-23 09:05:27 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.032 |  |
| 2026-02-23 09:01:30 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-23 09:06:16 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.042 |  |
| 2026-02-23 10:01:51 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.061 |  |
| 2026-02-23 09:06:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.066 |  |
| 2026-02-23 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.099 |  |
| 2026-02-23 09:03:06 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.127 |  |
| 2026-02-23 09:04:07 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.144 |  |
| 2026-02-23 09:03:57 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.290 |  |
| 2026-02-23 09:03:04 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.292 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)