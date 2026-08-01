# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_03:21:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 03:21:00 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -4.800 |  |
| 2026-08-02 03:20:53 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:20:45 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -4.800 |  |
| 2026-08-02 03:13:35 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:13:28 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:11:20 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:11:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-08-02 03:10:13 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.036 |  |
| 2026-08-02 03:10:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | -0.009 |  |
| 2026-08-02 03:09:29 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:07:42 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.085 |  |
| 2026-08-02 03:07:41 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:07:10 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-02 03:06:37 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.067 |  |
| 2026-08-02 03:06:28 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.130 |  |
| 2026-08-02 03:06:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.025 |  |
| 2026-08-02 03:06:02 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.393 |  |
| 2026-08-02 03:06:01 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:05:10 | Peradeniya (Mahaweli Ganga) | 3.13 | 🟢 Normal | -0.019 |  |
| 2026-08-02 03:05:05 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-02 03:04:50 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-08-02 03:04:45 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.237 |  |
| 2026-08-02 03:04:45 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:04:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-02 03:04:41 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.113 |  |
| 2026-08-02 03:04:17 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-02 03:04:01 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-08-02 03:03:53 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.125 |  |
| 2026-08-02 03:03:22 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:03:07 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:03:02 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:03:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:02:18 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-02 03:02:16 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:01:55 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:01:42 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.032 |  |
| 2026-08-02 03:01:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 03:11:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-08-02 03:02:18 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-02 03:07:10 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 03:02:16 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:20:53 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:03:07 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:03:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:06:01 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:11:20 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:13:35 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:13:28 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:07:41 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:04:45 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:03:02 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:09:29 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:01:55 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 03:10:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | -0.009 |  |
| 2026-08-02 03:04:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-02 03:01:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-02 03:04:17 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-02 03:05:05 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-02 03:05:10 | Peradeniya (Mahaweli Ganga) | 3.13 | 🟢 Normal | -0.019 |  |
| 2026-08-02 03:04:50 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-08-02 03:04:01 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-08-02 03:06:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.025 |  |
| 2026-08-02 03:01:42 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.032 |  |
| 2026-08-02 03:10:13 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.036 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-02 03:06:37 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.067 |  |
| 2026-08-02 03:07:42 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.085 |  |
| 2026-08-02 03:04:41 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.113 |  |
| 2026-08-02 03:03:53 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.125 |  |
| 2026-08-02 03:06:28 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.130 |  |
| 2026-08-02 03:04:45 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.237 |  |
| 2026-08-02 03:06:02 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.393 |  |
| 2026-08-02 03:21:00 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -4.800 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)