# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_00:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 00:03:31 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-02 00:03:12 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-08-02 00:02:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:42 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.081 |  |
| 2026-08-02 00:02:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:02:37 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.100 |  |
| 2026-08-02 00:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:24 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.053 |  |
| 2026-08-02 00:01:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:00:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:00:19 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:39:08 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:18:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 23:18:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 00:00:19 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:02:32 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:01:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:01:03 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:04:47 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:07:47 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:03:53 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:01:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:02:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:02:18 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:39:08 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 00:03:12 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:01:14 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:08:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-08-01 23:07:36 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-08-01 23:07:13 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-02 00:03:31 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-01 23:04:13 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.011 |  |
| 2026-08-01 23:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-08-01 23:03:46 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-08-02 00:00:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:02:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-08-02 00:02:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 23:07:52 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.043 |  |
| 2026-08-01 23:02:27 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-08-02 00:01:24 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.053 |  |
| 2026-08-02 00:02:42 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.081 |  |
| 2026-08-01 23:05:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.097 |  |
| 2026-08-02 00:02:37 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.100 |  |
| 2026-08-01 23:07:43 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.123 |  |
| 2026-08-01 23:05:10 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.163 |  |
| 2026-08-01 23:02:25 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | -0.210 |  |
| 2026-08-01 23:05:53 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.295 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)