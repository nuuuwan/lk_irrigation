# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_21:14:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,840 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 21:14:34 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:12:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-05-05 21:12:11 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:11:55 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-05 21:09:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:09:01 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |
| 2026-05-05 21:07:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:07:34 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 21:01:55 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-05-05 21:04:45 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-05 21:11:55 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-05 21:01:21 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-05 21:05:45 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 21:01:19 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 21:01:33 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 21:02:03 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 20:09:09 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 21:07:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:03:11 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:01:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:03:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:00:16 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 18:03:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:02:35 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:03:13 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:12:11 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:02:54 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 20:58:23 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:03:07 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:09:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:07:34 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:14:34 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-05 21:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-05 21:04:49 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.012 |  |
| 2026-05-05 21:12:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-05-05 21:04:52 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.019 |  |
| 2026-05-05 21:01:15 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.021 |  |
| 2026-05-05 21:04:26 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-05-05 21:05:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-05-05 21:03:47 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-05-05 21:02:23 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-05-05 21:05:29 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.050 |  |
| 2026-05-05 21:00:16 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.061 |  |
| 2026-05-05 21:06:13 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.072 |  |
| 2026-05-05 21:09:01 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)