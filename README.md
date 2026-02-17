# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_21:02:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,801 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 21:02:27 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:02:26 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-02-17 21:01:56 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-17 21:01:44 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 21:01:31 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-02-17 21:01:23 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:01:19 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:00:55 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:00:37 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:15:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -4.596 |  |
| 2026-02-17 20:11:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:11:15 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-02-17 20:11:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:10:27 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:10:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:09:43 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-17 20:08:56 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.117 |  |
| 2026-02-17 20:07:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:07:38 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -4.596 |  |
| 2026-02-17 20:07:30 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-17 20:07:13 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 20:05:28 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-02-17 18:03:50 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-17 20:09:43 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-17 21:01:44 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 21:00:37 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:00:55 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:01:19 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:01:23 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:04:10 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:02:27 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:07:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:03:33 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:02:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:02:32 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:04:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:11:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-17 21:02:26 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:02:46 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:10:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:07:13 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:04:21 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:02:34 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:11:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 20:07:30 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-17 20:02:39 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-17 20:02:19 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-17 21:01:31 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-02-17 21:01:56 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-17 20:00:56 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-02-17 20:11:15 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-02-17 21:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-02-17 20:04:04 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-02-17 20:03:18 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.032 |  |
| 2026-02-17 20:03:32 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.051 |  |
| 2026-02-17 20:08:56 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.117 |  |
| 2026-02-17 20:15:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -4.596 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)